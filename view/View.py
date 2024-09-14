class View:
    # แสดงสถานะของเครื่องรีดนม วัวที่ถูกจัดให้กับเครื่อง และปริมาณนมที่ผลิต
    def display_status(self, model, validator):
        print("Status of Machines:")
        
        # วนลูปเพื่อแสดงสถานะของแต่ละเครื่องรีดนมใน model
        for machine in model.machines:
            print(f"Machine {machine.id}: ({machine.current_cow}) : {machine.milking_heads}")  # แสดงเครื่องรีดนม ID, วัวปัจจุบัน และหัวรีดนม
        
        # แสดงจำนวนวัวที่รีดนมสำเร็จ
        print(f"วัวผลิตนมไปแล้ว: {model.success_milk} ตัว")
        
        # แสดงปริมาณนมที่ผลิตไปทั้งหมด
        print(f"ผลิตนมได้: {model.milk_produced} ลิตร")
        
        # แสดงจำนวนครั้งที่มีการแทรกแซงในกระบวนการ
        print(f"ถูกแทรกแซง: {validator.interventions} ครั้ง")

        print("------------------------------------------")
    
    # แสดงข้อความข้อผิดพลาดเมื่อเกิดปัญหาในกระบวนการรีดนม
    def show_error(self):
        print("ERROR DETECTED, remove problematic cow and reset process!")  # แสดงข้อความแจ้งเตือนข้อผิดพลาด
