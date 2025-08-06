frappe.pages['combined-view'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'بيانات الوعاظ',
		single_column: true
	});
}