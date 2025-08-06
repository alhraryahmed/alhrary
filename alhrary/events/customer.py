import frappe

def on_update_customer(doc, method):
    # تحديث الحقل custom_note
    doc.custom_note = "تم التحديث بواسطة Custom App Script"
    frappe.msgprint("Custom Script تم التنفيذ عند الحفظ")

