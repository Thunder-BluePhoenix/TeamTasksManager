frappe.listview_settings['Task'] = {
    add_fields: ['team', 'status', 'assigned_to'],
    onload: function(listview) {
        // Add CSS to the page
        const styleSheet = document.createElement("style");
        styleSheet.textContent = `
            .team-filter-wrapper {
                display: inline-block;
                margin-right: 10px;
                vertical-align: middle;
            }

            .team-filter-wrapper select {
                width: 150px;
                padding: 4px 8px;
                border-radius: 4px;
                border: 1px solid var(--border-color);
            }

            .filter-selector {
                margin-bottom: 15px;
                padding: 10px;
                border-radius: 4px;
                background-color: var(--fg-color);
                box-shadow: var(--shadow-sm);
            }

            .team-filter-header {
                display: flex;
                align-items: center;
                gap: 10px;
            }

            .team-filter-label {
                font-weight: 500;
                color: var(--text-color);
            }

            .team-names {
                display: flex;
                flex-wrap: wrap;
                gap: 5px;
            }

            .team-label {
                background-color: var(--alert-bg-success);
                color: var(--alert-text-success);
                padding: 2px 8px;
                border-radius: 12px;
                font-size: 12px;
            }

            .team-filter-loading {
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 10px;
            }

            .hidden {
                display: none;
            }
        `;
        document.head.appendChild(styleSheet);

        // Add loading indicator
        const loadingIndicator = $(`
            <div class="team-filter-loading">
                <span class="text-muted">Loading team filters...</span>
            </div>
        `).appendTo(listview.page.page_form);

        // Get current user's teams
        frappe.call({
            method: 'team_tasks_manager.team_tasks_manager.doctype.task.task.get_user_teams',
            callback: function(r) {
                loadingIndicator.remove();
                
                if (r.message && r.message.length > 0) {
                    const userTeams = r.message;
                    const teamCounts = {};

                    // Create filter dropdown
                    let $filterWrapper = $(`
                        <div class="team-filter-wrapper">
                            <select class="team-filter">
                                <option value="my_teams">My Teams</option>
                                <option value="all">All Tasks</option>
                                ${userTeams.map(team => `<option value="${team}">${team}</option>`).join('')}
                            </select>
                        </div>
                    `).appendTo(listview.page.page_form);

                    // Handle filter change
                    $filterWrapper.find('.team-filter').on('change', function() {
                        const selectedValue = $(this).val();
                        listview.filter_area.clear();

                        if (selectedValue === 'my_teams') {
                            listview.filter_area.add([
                                [listview.doctype, "team", "in", userTeams]
                            ]);
                        } else if (selectedValue !== 'all') {
                            listview.filter_area.add([
                                [listview.doctype, "team", "=", selectedValue]
                            ]);
                        }
                        listview.refresh();
                    });

                    // Initially filter for user's teams
                    listview.filter_area.add([
                        [listview.doctype, "team", "in", userTeams]
                    ]);
                    listview.refresh();

                    // Fetch and update team counts
                    userTeams.forEach(team => {
                        frappe.db.count('Task', {
                            filters: {team: team}
                        }).then(count => {
                            teamCounts[team] = count;
                            updateTeamCounts();
                        });
                    });

                    function updateTeamCounts() {
                        $('.team-filter option').each(function() {
                            const teamName = $(this).val();
                            if (teamCounts[teamName]) {
                                $(this).text(`${teamName} (${teamCounts[teamName]})`);
                            }
                        });
                    }

                } else {
                    frappe.msgprint({
                        title: __('No Team Assignment'),
                        message: __('You do not belong to any team. You may only see tasks assigned directly to you.'),
                        indicator: 'orange'
                    });
                }
            }
        });

        // Add refresh button
        listview.page.add_inner_button(__('Refresh Team Filters'), function() {
            listview.run();
        });

        // Add clear filter button
        listview.page.add_inner_button(__('Show All Tasks'), function() {
            $('.team-filter').val('all');
            listview.filter_area.clear();
            listview.refresh();
        });
    },
    get_indicator: function(doc) {
        const status_color = {
            'Open': 'red',
            'In Progress': 'orange',
            'Completed': 'green'
        };
        return [__(doc.status), status_color[doc.status], 'status,=,' + doc.status];
    }
};


