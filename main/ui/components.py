import lvgl as lv
class PageComponent:

    def __init__(self, comp_parent, pages, x, y):
        self.pages = pages
        self.page_idx = 0
        for page in self.pages:
            self.SetFlag(page, lv.obj.FLAG.HIDDEN, True)
        self.SetFlag(self.pages[self.page_idx], lv.obj.FLAG.HIDDEN, False)

        cui_Page_Container = lv.obj(comp_parent)
        cui_Page_Container.remove_style_all()
        cui_Page_Container.set_width(14)
        cui_Page_Container.set_height(10)
        cui_Page_Container.set_x(x)
        cui_Page_Container.set_y(y)
        cui_Page_Container.set_align(lv.ALIGN.CENTER)
        cui_Page_Container.set_flex_flow(lv.FLEX_FLOW.ROW)
        cui_Page_Container.set_flex_align(lv.FLEX_ALIGN.SPACE_AROUND, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.SPACE_AROUND)
        self.SetFlag(cui_Page_Container, lv.obj.FLAG.CLICKABLE, False)
        self.SetFlag(cui_Page_Container, lv.obj.FLAG.SCROLLABLE, False)
        self.pages_indactor=[]
        for page in pages:
            indactor = lv.btn(cui_Page_Container)
            indactor.set_width(4)
            indactor.set_height(4)
            indactor.set_align(lv.ALIGN.CENTER)
            self.SetFlag(indactor, lv.obj.FLAG.SCROLLABLE, False)
            self.SetFlag(indactor, lv.obj.FLAG.SCROLL_ON_FOCUS, True)
            self.pages_indactor.append(indactor)

        self.updatePageIndactor()

    def updatePageIndactor(self):
        for idx,indactor in enumerate(self.pages_indactor):
            if idx == self.page_idx:
                indactor.set_style_bg_color(lv.color_hex(0x3671C6), lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_color(lv.color_hex(0x3671C6), lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_width(5, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_spread(1, lv.PART.MAIN | lv.STATE.DEFAULT)
            else:
                indactor.set_style_bg_color(lv.color_hex(0x9A9A9A), lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_bg_opa(255, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_width(0, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_spread(0, lv.PART.MAIN | lv.STATE.DEFAULT)
                indactor.set_style_shadow_opa(0, lv.PART.MAIN | lv.STATE.DEFAULT)

    def nextPage(self):
        if self.page_idx + 1 >= len(self.pages):
            return
        self.SetFlag(self.pages[self.page_idx], lv.obj.FLAG.HIDDEN, True)
        self.page_idx += 1
        self.SetFlag(self.pages[self.page_idx], lv.obj.FLAG.HIDDEN, False)
        self.updatePageIndactor()
    def prePage(self):
        if self.page_idx - 1 < 0:
            return
        self.SetFlag(self.pages[self.page_idx], lv.obj.FLAG.HIDDEN, True)
        self.page_idx -= 1
        self.SetFlag(self.pages[self.page_idx], lv.obj.FLAG.HIDDEN, False)
        self.updatePageIndactor()

    def SetFlag(self, obj, flag, value):
        if (value):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def _ui_comp_del_event(self, e):
        target = e.get_target()
        self._ui_comp_table[id(target)].remove()

    def ui_comp_get_child(self, comp, child_name):
        return self._ui_comp_table[id(comp)][child_name]

    def ui_comp_get_root_from_child(self, child, compname):
        for component in self._ui_comp_table:
            if self._ui_comp_table[component]["_CompName"] == compname:
                for part in self._ui_comp_table[component]:
                    if id(self._ui_comp_table[component][part]) == id(child):
                        return self._ui_comp_table[component]
        return None

    def ModifyFlag(self, obj, flag, value):
        if (value == "TOGGLE"):
            if (obj.has_flag(flag)):
                obj.clear_flag(flag)
            else:
                obj.add_flag(flag)
            return

        if (value == "ADD"):
            obj.add_flag(flag)
        else:
            obj.clear_flag(flag)
        return

    def ModifyState(self, obj, state, value):
        if (value == "TOGGLE"):
            if (obj.has_state(state)):
                obj.clear_state(state)
            else:
                obj.add_state(state)
            return

        if (value == "ADD"):
            obj.add_state(state)
        else:
            obj.clear_state(state)
        return
