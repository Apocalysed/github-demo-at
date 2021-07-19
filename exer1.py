import re
str = 'Hai khu chung cư nằm trong khu vực "phố chung cư" ở Đà Nẵng. Các ca dương tính ghi nhận tại đây gồm "bệnh nhân 849, 853, 780, 781, 797 và 802". Từ 25/7 đến nay, Đà Nẵng đã ghi nhận 296 người mắc nCoV. Thành phố đang tiếp tục áp dụng cách ly xã hội theo chỉ thỉ 16 để khoanh vùng, dập dịch.'
a = re.findall(r'[\w+\d\sa-zA-Z0-9]+[.,""]',str)
print(a)