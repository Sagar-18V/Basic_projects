import uiautomator2 as u2
d = u2.connect('mobile-serial')  # get from "adb devices"
print(d.info)