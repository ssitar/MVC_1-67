from model.MachineModel import Machine

class Model:
    def __init__(self):
        # กำหนดคิววัวที่รอรีดนม, วัวที่อยู่ในเครื่องรีดนม, เครื่องรีดนม, จำนวนเครื่องที่พร้อมใช้งาน
        self.cows_queue = []  # คิววัวที่รอเข้าเครื่องรีดนม
        self.cows_current = []  # วัวที่กำลังอยู่ในเครื่องรีดนม
        self.machines = [Machine(i) for i in range(10)]  # สร้างเครื่องรีดนม 10 เครื่อง
        self.ready_machine = 10  # จำนวนเครื่องรีดนมที่พร้อมใช้งาน
        self.milk_produced = 0  # ปริมาณนมที่ผลิตไปแล้ว
        self.success_milk = 0  # จำนวนวัวที่รีดนมสำเร็จ
    
    # ฟังก์ชันรีเซ็ตสถานะทั้งหมดของระบบ
    def reset(self):
        self.cows_current = []  # ล้างลิสต์วัวที่อยู่ในเครื่องรีดนม
        self.machines = [Machine(i) for i in range(10)]  # รีเซ็ตเครื่องรีดนมทั้งหมด
        self.ready_machine = 10  # รีเซ็ตจำนวนเครื่องที่พร้อมใช้งาน
    
    # ฟังก์ชันจัดวัวเข้ากับเครื่องรีดนมที่ว่างอยู่
    def fit_cows_to_machines(self):
        # จัดวัวเข้ากับเครื่องรีดนมในขณะที่ยังมีเครื่องที่พร้อมใช้งานและยังมีวัวในคิว
        while self.ready_machine > 0 and self.cows_queue:
            cow = self.cows_queue.pop(0)  # ดึงวัวจากคิว
            target_machine = cow.target_machine  # เครื่องที่วัวต้องการเข้ารับการรีดนม
            
            # ถ้าเครื่องเป้าหมายว่าง ให้วัวเข้าเครื่อง
            if self.machines[target_machine].current_cow is None:
                self.machines[target_machine].current_cow = cow  # จัดวัวเข้ากับเครื่องเป้าหมาย
                self.ready_machine -= 1  # ลดจำนวนเครื่องที่พร้อมใช้งาน
                self.cows_current.append(cow)  # เพิ่มวัวลงในลิสต์วัวที่อยู่ในเครื่องรีดนม
            else:
                # ถ้าเครื่องเป้าหมายไม่ว่าง ให้หาวัวเครื่องอื่นที่ว่าง
                for i in range(1, 10):
                    target_machine = (target_machine + i) % 10  # วนหาเครื่องว่าง
                    if self.machines[target_machine].current_cow is None:
                        self.machines[target_machine].current_cow = cow  # จัดวัวเข้ากับเครื่องว่าง
                        self.ready_machine -= 1  # ลดจำนวนเครื่องที่พร้อมใช้งาน
                        self.cows_current.append(cow)  # เพิ่มวัวลงในลิสต์วัวที่อยู่ในเครื่องรีดนม
                        break
    
    # ฟังก์ชันรีดนมจากเครื่องที่กำหนด
    def do_milk(self, machine):
        # ผลิตนม 1 ลิตรถ้าเครื่องรีดตรงกับเครื่องเป้าหมายของวัว มิฉะนั้น ผลิตได้ 0.5 ลิตร
        self.milk_produced += 1 if machine.id == machine.current_cow.target_machine else 0.5
        self.ready_machine += 1  # เพิ่มจำนวนเครื่องที่พร้อมใช้งาน
        self.success_milk += 1  # เพิ่มจำนวนวัวที่รีดนมสำเร็จ
        machine.reset()  # รีเซ็ตเครื่องรีดนมหลังจากรีดนมเสร็จ
    
    # ฟังก์ชันจัดการกับวัวที่มีปัญหา
    def kick_error_cow(self, cow):
        self.cows_current.remove(cow)  # เอาวัวที่มีปัญหาออกจากลิสต์วัวที่อยู่ในเครื่องรีดนม
        self.cows_queue = self.cows_current + self.cows_queue  # เพิ่มวัวที่เหลือกลับเข้าไปในคิว
