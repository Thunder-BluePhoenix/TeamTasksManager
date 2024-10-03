// frappe.pages['task-dashboard'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Task Dashboard',
// 		single_column: true
// 	});
// }

frappe.pages['task-dashboard'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Task Dashboard',
        single_column: true
    });
    
    page.add_inner_button('Refresh', () => load_dashboard(page));
    load_dashboard(page);
}

function load_dashboard(page) {
    frappe.call({
        method: 'team_tasks_manager.team_tasks_manager.page.task_dashboard.task_dashboard.get_dashboard_data',
        callback: function(r) {
            let data = r.message;
            render_dashboard(page, data);
        }
    });
}

function render_dashboard(page, data) {
    let $content = $(page.body).empty();
    
    // Render team-wise task count
    let $teamSection = $(`<div>
        <h3>Tasks by Team</h3>
        <div id="team-chart"></div>
    </div>`).appendTo($content);
    
    // Render status distribution
    let $statusSection = $(`<div>
        <h3>Task Status Distribution</h3>
        <div id="status-chart"></div>
    </div>`).appendTo($content);
    
    // Create charts using Chart.js or any other library
    // For simplicity, we'll just show the data in a table format
    let $teamTable = $(`<table class="table table-bordered">
        <tr><th>Team</th><th>Task Count</th></tr>
        ${Object.entries(data.team_wise_count).map(([team, count]) => 
            `<tr><td>${team}</td><td>${count}</td></tr>`
        ).join('')}
    </table>`).appendTo($teamSection);
    
    let $statusTable = $(`<table class="table table-bordered">
        <tr><th>Status</th><th>Count</th></tr>
        ${Object.entries(data.status_distribution).map(([status, count]) => 
            `<tr><td>${status}</td><td>${count}</td></tr>`
        ).join('')}
    </table>`).appendTo($statusSection);
}
