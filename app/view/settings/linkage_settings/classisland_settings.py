# ==================================================
# 导入库
# ==================================================

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtNetwork import *
from qfluentwidgets import *

from app.tools.variable import *
from app.tools.path_utils import *
from app.tools.personalised import *
from app.tools.settings_default import *
from app.tools.settings_access import *
from app.Language.obtain_language import *


# ==================================================
# ClassIsland 通知服务设置
# ==================================================
class classisland_settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 创建垂直布局
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.vBoxLayout.setSpacing(10)

        # 添加点名 ClassIsland 通知服务设置组件
        self.roll_call_classisland_widget = (
            roll_call_classisland_notification_service_settings(self)
        )
        self.vBoxLayout.addWidget(self.roll_call_classisland_widget)

        # 添加闪抽 ClassIsland 通知服务设置组件
        self.quick_draw_classisland_widget = (
            quick_draw_classisland_notification_service_settings(self)
        )
        self.vBoxLayout.addWidget(self.quick_draw_classisland_widget)

        # 添加抽奖 ClassIsland 通知服务设置组件
        self.lottery_classisland_widget = (
            lottery_classisland_notification_service_settings(self)
        )
        self.vBoxLayout.addWidget(self.lottery_classisland_widget)


class roll_call_classisland_notification_service_settings(GroupHeaderCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle(
            get_content_name_async(
                "classisland_settings",
                "roll_call_notification_service_settings",
            )
        )
        self.setBorderRadius(8)

        # 通知服务类型选择
        self.notification_service_type_combo_box = ComboBox()
        self.notification_service_type_combo_box.addItems(
            get_content_combo_name_async(
                "classisland_settings", "roll_call_notification_service_type"
            )
        )
        self.notification_service_type_combo_box.setCurrentIndex(
            readme_settings_async(
                "roll_call_notification_settings", "notification_service_type"
            )
        )
        self.notification_service_type_combo_box.currentIndexChanged.connect(
            self.on_notification_service_type_changed
        )

        # 通知显示时长
        self.notification_display_duration_spinbox = SpinBox()
        self.notification_display_duration_spinbox.setFixedWidth(WIDTH_SPINBOX)
        self.notification_display_duration_spinbox.setRange(1, 60)
        self.notification_display_duration_spinbox.setSuffix("s")
        self.notification_display_duration_spinbox.setValue(
            readme_settings_async(
                "roll_call_notification_settings", "notification_display_duration"
            )
        )
        self.notification_display_duration_spinbox.valueChanged.connect(
            lambda: update_settings(
                "roll_call_notification_settings",
                "notification_display_duration",
                self.notification_display_duration_spinbox.value(),
            )
        )

        # 添加设置项到分组
        self.addGroup(
            get_theme_icon("ic_fluent_cloud_20_filled"),
            get_content_name_async(
                "classisland_settings", "roll_call_notification_service_type"
            ),
            get_content_description_async(
                "classisland_settings", "roll_call_notification_service_type"
            ),
            self.notification_service_type_combo_box,
        )
        self.addGroup(
            get_theme_icon("ic_fluent_timer_20_filled"),
            get_content_name_async(
                "classisland_settings", "roll_call_notification_display_duration"
            ),
            get_content_description_async(
                "classisland_settings", "roll_call_notification_display_duration"
            ),
            self.notification_display_duration_spinbox,
        )

    def on_notification_service_type_changed(self, index):
        """通知服务类型变化时的处理"""
        update_settings(
            "roll_call_notification_settings",
            "notification_service_type",
            index,
        )
        # 如果选择了ClassIsland或内置+ClassIsland，显示提示信息
        if index == 1 or index == 2:
            from qfluentwidgets import InfoBar, InfoBarPosition

            hint_title = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "title",
            )
            hint_content = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "content",
            )

            InfoBar.success(
                title=hint_title,
                content=hint_content,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=5000,
                parent=self,
            )


class quick_draw_classisland_notification_service_settings(GroupHeaderCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle(
            get_content_name_async(
                "classisland_settings",
                "quick_draw_notification_service_settings",
            )
        )
        self.setBorderRadius(8)

        # 通知服务类型选择
        self.notification_service_type_combo_box = ComboBox()
        self.notification_service_type_combo_box.addItems(
            get_content_combo_name_async(
                "classisland_settings", "quick_draw_notification_service_type"
            )
        )
        self.notification_service_type_combo_box.setCurrentIndex(
            readme_settings_async(
                "quick_draw_notification_settings", "notification_service_type"
            )
        )
        self.notification_service_type_combo_box.currentIndexChanged.connect(
            self.on_notification_service_type_changed
        )

        # 通知显示时长
        self.notification_display_duration_spinbox = SpinBox()
        self.notification_display_duration_spinbox.setFixedWidth(WIDTH_SPINBOX)
        self.notification_display_duration_spinbox.setRange(1, 60)
        self.notification_display_duration_spinbox.setSuffix("s")
        self.notification_display_duration_spinbox.setValue(
            readme_settings_async(
                "quick_draw_notification_settings", "notification_display_duration"
            )
        )
        self.notification_display_duration_spinbox.valueChanged.connect(
            lambda: update_settings(
                "quick_draw_notification_settings",
                "notification_display_duration",
                self.notification_display_duration_spinbox.value(),
            )
        )

        # 添加设置项到分组
        self.addGroup(
            get_theme_icon("ic_fluent_cloud_20_filled"),
            get_content_name_async(
                "classisland_settings", "quick_draw_notification_service_type"
            ),
            get_content_description_async(
                "classisland_settings", "quick_draw_notification_service_type"
            ),
            self.notification_service_type_combo_box,
        )
        self.addGroup(
            get_theme_icon("ic_fluent_timer_20_filled"),
            get_content_name_async(
                "classisland_settings", "quick_draw_notification_display_duration"
            ),
            get_content_description_async(
                "classisland_settings", "quick_draw_notification_display_duration"
            ),
            self.notification_display_duration_spinbox,
        )

    def on_notification_service_type_changed(self, index):
        """通知服务类型变化时的处理"""
        update_settings(
            "quick_draw_notification_settings",
            "notification_service_type",
            index,
        )
        # 如果选择了ClassIsland或内置+ClassIsland，显示提示信息
        if index == 1 or index == 2:
            from qfluentwidgets import InfoBar, InfoBarPosition

            hint_title = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "title",
            )
            hint_content = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "content",
            )

            InfoBar.success(
                title=hint_title,
                content=hint_content,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=5000,
                parent=self,
            )


class lottery_classisland_notification_service_settings(GroupHeaderCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle(
            get_content_name_async(
                "classisland_settings",
                "lottery_notification_service_settings",
            )
        )
        self.setBorderRadius(8)

        # 通知服务类型选择
        self.notification_service_type_combo_box = ComboBox()
        self.notification_service_type_combo_box.addItems(
            get_content_combo_name_async(
                "classisland_settings", "lottery_notification_service_type"
            )
        )
        self.notification_service_type_combo_box.setCurrentIndex(
            readme_settings_async(
                "lottery_notification_settings", "notification_service_type"
            )
        )
        self.notification_service_type_combo_box.currentIndexChanged.connect(
            self.on_notification_service_type_changed
        )

        # 通知显示时长
        self.notification_display_duration_spinbox = SpinBox()
        self.notification_display_duration_spinbox.setFixedWidth(WIDTH_SPINBOX)
        self.notification_display_duration_spinbox.setRange(1, 60)
        self.notification_display_duration_spinbox.setSuffix("s")
        self.notification_display_duration_spinbox.setValue(
            readme_settings_async(
                "lottery_notification_settings", "notification_display_duration"
            )
        )
        self.notification_display_duration_spinbox.valueChanged.connect(
            lambda: update_settings(
                "lottery_notification_settings",
                "notification_display_duration",
                self.notification_display_duration_spinbox.value(),
            )
        )

        # 添加设置项到分组
        self.addGroup(
            get_theme_icon("ic_fluent_cloud_20_filled"),
            get_content_name_async(
                "classisland_settings", "lottery_notification_service_type"
            ),
            get_content_description_async(
                "classisland_settings", "lottery_notification_service_type"
            ),
            self.notification_service_type_combo_box,
        )
        self.addGroup(
            get_theme_icon("ic_fluent_timer_20_filled"),
            get_content_name_async(
                "classisland_settings", "lottery_notification_display_duration"
            ),
            get_content_description_async(
                "classisland_settings", "lottery_notification_display_duration"
            ),
            self.notification_display_duration_spinbox,
        )

    def on_notification_service_type_changed(self, index):
        """通知服务类型变化时的处理"""
        update_settings(
            "lottery_notification_settings",
            "notification_service_type",
            index,
        )
        # 如果选择了ClassIsland或内置+ClassIsland，显示提示信息
        if index == 1 or index == 2:
            from qfluentwidgets import InfoBar, InfoBarPosition

            hint_title = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "title",
            )
            hint_content = get_any_position_value_async(
                "classisland_settings",
                "classisland_notification_hint",
                "content",
            )

            InfoBar.success(
                title=hint_title,
                content=hint_content,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=5000,
                parent=self,
            )
