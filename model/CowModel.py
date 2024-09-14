class Cow:
    def __init__(self, id, target_machine, no_udder=4, is_male=False):
        # กำหนดคุณสมบัติของวัว เช่น ID, เครื่องรีดนมที่เป็นเป้าหมาย, จำนวนเต้านม, เพศ
        self.id = id  # รหัสประจำตัวของวัว
        self.no_udder = no_udder  # จำนวนเต้านมของวัว
        self.is_male = is_male  # กำหนดเพศของวัว ถ้าเป็นผู้ชายค่า is_male จะเป็น True
        self.target_machine = target_machine  # เครื่องรีดนมที่วัวควรจะไป
        self.milk_produced = 0  # ปริมาณนมที่วัวผลิตได้เริ่มต้นที่ 0
        self.state = "waiting"  # สถานะของวัว (เริ่มต้นที่กำลังรอ)
        self.udders = list()  # ลิสต์สำหรับเก็บสถานะของแต่ละเต้านม
        
        # สร้างลิสต์เก็บสถานะของเต้านมวัว (True = มีเต้านม, False = ไม่มีเต้านม)
        for i in range(no_udder):
            self.udders.append(True)  # เพิ่มเต้านมที่ใช้งานได้ (True) ตามจำนวนที่กำหนด
        for i in range(4-no_udder):
            self.udders.append(False)  # ถ้ามีเต้านมน้อยกว่า 4 ให้เติม False เพื่อให้ครบ 4 เต้า
    
    # ฟังก์ชันสำหรับแสดงผลข้อมูลวัวในรูปแบบ string
    def __str__(self):
        # แสดงข้อมูลของวัว เช่น รหัสประจำตัว เพศ จำนวนเต้านม และเครื่องรีดนมเป้าหมาย
        return f"Cow id : {self.id}, sex : {'M' if self.is_male else 'F' }, no_udder : {self.no_udder}, target : {self.target_machine}"
