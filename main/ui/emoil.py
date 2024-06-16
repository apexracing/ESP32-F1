import lvgl as lv
from ui.resource_manager import ResourceManager


class Emoil:
    '''
        使用https://app.lottiefiles.com/制作动画文件
        每个表情都为前5帧都为从其它表情的过滤动画，剩余为表情主体动画,过渡动画只播放1次，主体动画循环播放
        :param lv_obj 添加动画的容器Container
        :param raw_file 动画表情文件
        :param skip_trans 是否跳过过渡动画,如果为True,last_emoil将会直接跳过
        :param last_emoil 如果不为None,从一个表情过渡到另一个表情时，需要等侍上一个表情播完后，播放当前表情
    '''

    def __init__(self, lv_obj, raw_file,width=150,height=80):
        self.parent = lv_obj
        self.width=width
        self.height=height
        self.resourceManager = ResourceManager()
        self._raw_file=raw_file
        self.lottie_data = self.resourceManager.load_raw(self._raw_file)
        self._lottie=None
        self.play() 

    def play(self):
        self.parent.clean()
        self._lottie = lv.rlottie_create_from_raw(self.parent, self.width, self.height,self.lottie_data)
        lv.rlottie_set_play_mode(self._lottie, lv.RLOTTIE_CTRL.LOOP)
        self._lottie.set_width(lv.SIZE.CONTENT)  # 1
        self._lottie.set_height(lv.SIZE.CONTENT)  # 1
        self._lottie.set_align(lv.ALIGN.CENTER)

    @property
    def lottie(self):
        return self._lottie
    @property
    def raw_file(self):
        return self._raw_file
