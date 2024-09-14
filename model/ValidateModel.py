class ValidateModel:
    def __init__(self) -> None:
        # เก็บจำนวนครั้งที่เกิดการแทรกแซงและรายชื่อวัวที่มีปัญหา
        self.interventions = 0  # จำนวนครั้งที่มีการแทรกแซงในกระบวนการรีดนม
        self.problematic_cows = []  # ลิสต์เก็บวัวที่มีปัญหา
    
    # ฟังก์ชันเรียกเมื่อพบข้อผิดพลาดในกระบวนการ
    def error_detected(self, error_cow):
        self.interventions += 1  # เพิ่มจำนวนการแทรกแซง
        self.problematic_cows.append(error_cow)  # เพิ่มวัวที่มีปัญหาลงในลิสต์
    
    # ฟังก์ชันตรวจสอบเพศของวัวในเครื่องรีดนม
    def validate_sex(self, model):
        for machine in model.machines:
            # ตรวจสอบว่าเครื่องมีวัวปัจจุบันและวัวนั้นเป็นเพศผู้หรือไม่
            if machine.current_cow and machine.current_cow.is_male:
                self.error_detected(machine.current_cow)  # ตรวจพบข้อผิดพลาด วัวเพศผู้ไม่สามารถรีดนมได้
                return machine.current_cow  # คืนค่าวัวที่มีปัญหา
        return None  # ถ้าไม่มีวัวเพศผู้ คืนค่า None
    
    # ฟังก์ชันตรวจสอบกระบวนการรีดนมว่าถูกต้องหรือไม่
    def validate_milking_process(self, machine, i):
        cow = machine.current_cow  # ดึงข้อมูลวัวในเครื่องรีดนม
        # ตรวจสอบว่าวัวมีจำนวนเต้านมที่เพียงพอหรือไม่เมื่อเทียบกับหัวรีดนม
        if cow.no_udder <= i:
            self.error_detected(cow)  # ถ้าจำนวนเต้านมไม่เพียงพอ ตรวจพบข้อผิดพลาด
            return False  # คืนค่า False แสดงว่ากระบวนการไม่ถูกต้อง
        return True  # คืนค่า True ถ้ากระบวนการถูกต้อง
