import lvgl as lv
from common.resource_manager import ResourceManager


class Emoil:
    '''
        使用https://app.lottiefiles.com/制作动画文件
        每个表情都为前5帧都为从其它表情的过滤动画，剩余为表情主体动画,过渡动画只播放1次，主体动画循环播放
        :param lv_obj 添加动画的容器Container
        :param raw_file 动画表情文件
        :param skip_trans 是否跳过过渡动画,如果为True,last_emoil将会直接跳过
        :param last_emoil 如果不为None,从一个表情过渡到另一个表情时，需要等侍上一个表情播完后，播放当前表情
    '''

    def __init__(self, lv_obj, raw_file,width=150,height=80, skip_trans=True, last_emoil=None):
        self.parent = lv_obj
        self.width=width
        self.height=height
        self.last_emoil = last_emoil
        self.skip_trans = skip_trans
        self.resourceManager = ResourceManager()
        self.raw_file=raw_file

        lottie_data = self.resourceManager.load_raw(raw_file)
        if skip_trans:
            self.play_main()
        else:
            if last_emoil is None:
                self.play_head()
            else:
                self.last_emoil.lottie.add_event_cb(self.lottie_eventhandler, lv.EVENT.ALL, None)

    def lottie_eventhandler(self, event_struct):
        event = event_struct.code
        target = event_struct.target
        if event == lv.EVENT.READY and target == self.lottie:
            self.play_main()
        if event == lv.EVENT.READY and target == self.last_emoil.lottie:
            self.play_head()
        return

    def play_head(self):
        self.parent.clean()
        self.lottie = lv.rlottie_create_from_raw_range(self.parent, self.width, self.height, self.raw_file, 0, 5)
        lv.rlottie_set_play_mode(self.lottie, lv.RLOTTIE_CTRL.PLAY)
        self.lottie.set_width(lv.SIZE.CONTENT)  # 1
        self.lottie.set_height(lv.SIZE.CONTENT)  # 1
        self.lottie.set_align(lv.ALIGN.CENTER)
        self.lottie.add_event_cb(self.lottie_eventhandler, lv.EVENT.ALL, None)

    def play_main(self):
        self.parent.clean()
        lottie_data = self.resourceManager.load_raw(self.raw_file)
        self.lottie = lv.rlottie_create_from_raw_range(self.parent, self.width, self.height, self.raw_file, 5,0)
        lv.rlottie_set_play_mode(self.lottie, lv.RLOTTIE_CTRL.LOOP)
        self.lottie.set_width(lv.SIZE.CONTENT)  # 1
        self.lottie.set_height(lv.SIZE.CONTENT)  # 1
        self.lottie.set_align(lv.ALIGN.CENTER)

    @property
    def value(self):
        return self.lottie
