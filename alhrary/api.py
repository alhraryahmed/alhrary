import frappe

def sync_workflow_state(doc, method):
    # البحث عن السجلات المرتبطة في Data pre
    related_data_pre = frappe.get_all("Data pre", filters={"lagna_reference": doc.name}, fields=["name", "workflow_state"])

    for record in related_data_pre:
        if doc.workflow_state_lagna == "معتمد" and record.workflow_state == "جديد":
            state_name = frappe.db.get_value("Workflow State", {"state": "مستمر"}, "name")
            if state_name:
                frappe.db.set_value("Data pre", record.name, "workflow_state", state_name)

        elif doc.workflow_state_lagna == "مرفوض" and record.workflow_state == "جديد":
            state_name = frappe.db.get_value("Workflow State", {"state": "منقطع"}, "name")
            if state_name:
                frappe.db.set_value("Data pre", record.name, "workflow_state", state_name)

