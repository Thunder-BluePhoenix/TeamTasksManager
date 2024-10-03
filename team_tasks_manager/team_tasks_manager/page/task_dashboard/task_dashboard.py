import frappe

@frappe.whitelist()
def get_dashboard_data():
    team_wise_count = frappe.db.sql("""
        SELECT team, COUNT(*) as count
        FROM `tabTask`
        GROUP BY team
    """, as_dict=True)
    
    status_distribution = frappe.db.sql("""
        SELECT status, COUNT(*) as count
        FROM `tabTask`
        GROUP BY status
    """, as_dict=True)
    
    return {
        "team_wise_count": {t.team: t.count for t in team_wise_count},
        "status_distribution": {s.status: s.count for s in status_distribution}
    }

