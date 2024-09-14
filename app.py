import random

# นำเข้าโมดูลที่จำเป็นสำหรับ Model, CowModel, Validator, View และ Controller
from model.Model import Model
from model.CowModel import Cow as CowModel
from model.ValidateModel import ValidateModel as Validator
from view.View import View
from controller.Controller import Controller

# ฟังก์ชันสุ่มรายการวัว พร้อมกำหนดคุณสมบัติที่แตกต่างกัน
def random_cow(n, LESS_UDDER_RATE, MORE_UDDER_RATE, FALSE_UDDER_RATE):
    cowList = list()  # สร้างลิสต์ว่างเพื่อเก็บวัวแต่ละตัว
    
    for i in range(n):
        rand = random.randint(0, 99)  # สุ่มค่าตั้งแต่ 0 ถึง 99
        cow = CowModel(id=i, target_machine=int(rand/10))  # สร้างวัวพร้อม ID และ target_machine
        
        # ตรวจสอบอัตราการสุ่มเพื่อกำหนดจำนวนเต้านมและเพศ
        if (rand < LESS_UDDER_RATE):
            cow.no_udder = 3  # กำหนดจำนวนเต้านมเป็น 3
        elif (rand < LESS_UDDER_RATE + MORE_UDDER_RATE):
            cow.no_udder = 5  # กำหนดจำนวนเต้านมเป็น 5
        elif (rand < LESS_UDDER_RATE + MORE_UDDER_RATE + FALSE_UDDER_RATE):
            cow.is_male = True  # กำหนดเพศของวัวเป็นผู้ชาย
        
        cowList.append(cow)  # เพิ่มวัวลงในลิสต์
    
    return cowList  # คืนค่าลิสต์วัวทั้งหมด

# ฟังก์ชันหลักสำหรับการจัดการการรีดนม
def main():
    # สร้างอ็อบเจ็กต์ model, view, validator และ controller
    model = Model()
    view = View()
    validator = Validator()
    controller = Controller(model, view, validator)    
    
    # กำหนดอัตราการสุ่มเต้านมและเพศของวัว
    (LESS_UDDER_RATE, MORE_UDDER_RATE, FALSE_UDDER_RATE) = (2, 1, 2)
    
    # สร้างรายการวัว 100 ตัวพร้อมคุณสมบัติแบบสุ่ม
    cowList = random_cow(100, LESS_UDDER_RATE, MORE_UDDER_RATE, FALSE_UDDER_RATE)
    
    # เพิ่มวัวแต่ละตัวลงในคิวของ controller
    for cow in cowList:
        controller.add_cow_to_queue(cow)

    # วนลูปเพื่อจัดวัวเข้ากับเครื่องรีดนมและแสดงสถานะ
    while True:
        controller.fit_cows_to_machines()  # จัดวัวเข้ากับเครื่องรีดนม
        controller.display_status(model)  # แสดงสถานะของ model
        
        # รับข้อมูลจากผู้ใช้
        ip = input("press enter to process milk(type \"exit\" to exit): ")
        
        # ถ้าผู้ใช้พิมพ์ exit จะออกจากลูป
        if ip == 'exit':
            break
        
        controller.process_milking()  # ดำเนินการรีดนม

# เริ่มโปรแกรมเมื่อไฟล์นี้ถูกเรียกใช้งานโดยตรง
if __name__ == '__main__':
    main()
