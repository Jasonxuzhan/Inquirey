"""
    客户信息登记
    功能模块
    copyright by jason.xu 2023 
"""
import os
import json

class CustomerInfo:
    """客户基本信息"""
   
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.customer_info = {}
        self.work_path = os.makedirs(os.getcwd() + "\\" + self.customer_name)
    
    #建立客户基本信息，返回dict
    def customer_info_record(self):
        """Generate customer info dict, return dict"""
        print("客户信息不完整时，请用*号代替，以保持数据完整性" )
        self.customer_info["source_from"] = input("请输入线索来源: ")
        self.customer_info["source_channel"] = input("请输入来源渠道: ")
        self.customer_info["province"] = input("请输入省份，直辖市可在此输入: ")
        self.customer_info["city"] = input("请输入城市: ")
        self.customer_info["company"] = self.customer_name
        self.customer_info["name"] = input("请输入姓名: ")
        self.customer_info["telephone"] = input("请输入电话号码: ")
        self.customer_info["scenario"] = input("请输入应用场景: ")
        self.customer_info["cooperate_term"] = input("请输入合作方式: ")
        self.customer_info["request_desc"] = input("需求描述: ")
        self.customer_info["answer_by"] = input("接线员姓名: ")
        self.customer_info["transfer_to"] = input("业务人员姓名: ")
        for j, k in self.customer_info.items():
            print(j + ":" + k) 
        return self.customer_info

    #保存客户信息 
    def customer_info_save(self):
        """Save as json file"""
        with open(f"{self.current_path}\\{self.customer_name}.json", "w", encoding='utf-8') as f:
            json.dump(self.customer_info, f, indent=2, ensure_ascii=False)

    #读取客户信息
    def customer_info_read(self):
       """读取指定的json文件"""
       with open(f"{self.customer_name}.json", "r", encoding='utf-8') as f:
            data = json.load(f)
            return data 
    
    #修改客户信息
    def customer_info_update(self):
        """修改指定的json文件, 进入循环修改字典的value, 并保存"""
        with open(f"{self.customer_name}.json", "r", encoding='utf-8') as f:
            data = json.load(f)
        while True:
            key = input("Pls input key name or input q to quit: ")
            if key == "q":
                break
            elif key in list(i for i in data.keys()):
                data[key] = input("pls input update info according to the key: ")
            else:
                continue
        with open(f"{self.customer_name}.json", "w", encoding='utf-8') as f:
            update_data = json.dump(data, f, indent=2, ensure_ascii=False)
        return update_data        






if __name__ == "__main__":
    xinya = CustomerInfo("xinya")
    xinya.customer_info_record()
    xinya.customer_info_save()
    

    



















        




