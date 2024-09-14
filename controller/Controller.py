class Controller:
    def __init__(self, model, view, validator):
        # กำหนดตัวแปรอ้างอิงไปยัง model, view และ validator
        self.model = model  # อ้างอิงถึง model สำหรับเก็บข้อมูลของระบบ
        self.view = view  # อ้างอิงถึง view สำหรับแสดงสถานะ
        self.validator = validator  # อ้างอิงถึง validator สำหรับตรวจสอบความถูกต้อง
    
    # เพิ่มวัวลงในคิวรอรีดนม
    def add_cow_to_queue(self, cow):
        self.model.cows_queue.append(cow)  # เพิ่มวัวลงในคิวของ model
    
    # แสดงสถานะปัจจุบันของระบบผ่าน view
    def display_status(self, model):
        self.view.display_status(model, self.validator)  # แสดงข้อมูลจาก model และ validator
    
    # จัดการกับวัวที่เกิดปัญหา
    def error_handler(self, error_cow):
        self.model.kick_error_cow(error_cow)  # เอาวัวที่มีปัญหาออกจากระบบ
        self.model.reset()  # รีเซ็ตระบบกลับไปสู่สถานะเริ่มต้น
        self.view.show_error()  # แสดงข้อความแจ้งเตือนผ่าน view
    
    # จัดวัวเข้ากับเครื่องรีดนมที่พร้อมใช้งาน
    def fit_cows_to_machines(self):
        self.model.fit_cows_to_machines()  # พยายามจัดวัวจากคิวเข้าเครื่องรีดนม
        err = self.validator.validate_sex(self.model)  # ตรวจสอบเพศของวัว
        if err:
            self.error_handler(err)  # ถ้าวัวเป็นเพศผู้ ให้จัดการกับปัญหา
    
    # จำลองกระบวนการรีดนม
    def process_milking(self):
        # วนลูปผ่านเครื่องรีดนมทั้งหมดใน model
        for machine in self.model.machines:
            if machine.current_cow is None:
                continue  # ถ้าไม่มีวัวในเครื่องนี้ ให้ข้ามไป
            flag = False
            # ตรวจสอบหัวรีดนมทีละเต้า
            for i in range(len(machine.milking_heads)):
                if machine.milking_heads[i] == "cleaning":
                    machine.milking_heads[i] = "ready"  # เปลี่ยนสถานะจาก cleaning เป็น ready
                if not flag and machine.milking_heads[i] == "idle":
                    # ตรวจสอบว่าหัวรีดนมสามารถใช้งานได้หรือไม่
                    if self.validator.validate_milking_process(machine, i):
                        machine.milking_heads[i] = "cleaning"  # เปลี่ยนสถานะเป็น cleaning ถ้าผ่านการตรวจสอบ
                        flag = True
                    else:
                        # ถ้ามีปัญหา ให้จัดการวัวที่เกิดปัญหา
                        self.error_handler(machine.current_cow)
                        break
            # ถ้าหัวรีดนมทั้งหมดพร้อม ให้ทำการรีดนม
            if machine.milking_heads[3] == "ready":
                for i in range(len(machine.milking_heads)):
                    machine.milking_heads[i] = "milking"  # เปลี่ยนสถานะเป็น milking สำหรับการรีดนม
                self.model.do_milk(machine)  # ดำเนินการรีดนม
