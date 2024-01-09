"""
    客户项目跟踪信息
    功能模块
    copyright by jason.xu 2023 
"""
import os
import json
from datetime import datetime
now = datetime.now().strftime("%Y-%m-%d %H: %M :%S")


class CustomerProject:
    """Creat customer project comment, status"""

    def __init__(self, customer_name, project_name):
        """初始化公司名称、项目名称、跟踪记录、跟踪记录列表"""
        self.customer_name = customer_name
        self.project_name = project_name
        self.comment = ""
        self.comments_dict = {}
        self.project_status = "follow"
        self.customer_path = ""
  
    def creat_comment(self):
        """Add first comment for project, return dict""" 
        if self.project_status == "follow":
            self.comment = input(f"Pls input {self.project_name} first comment: ")
            self.comments_dict[now] = self.comment
            with open(f"{self.project_name}.json", "w", encoding="utf-8") as f:
                json.dump(self.comments_dict, f, indent=2, ensure_ascii=False)
                print(f"first comment: {self.comment}")
        else:
            print("pls adjust the status to \"follow\" that comment can be added")
        return self.comments_dict


    def project_status_revise(self):
        """default is follow, return string"""
        status = input(f"Pls input {self.project_name} current status ")
        if status not in ["follow","closed","give up"]:
            print("Input is wrong!")
        else:
            self.project_status = status   
            print(f"current is: {self.project_status}")
        return self.project_status


    def comment_add(self):
        """comment saved in existed json file, retrun dict """
        with open(f"{self.project_name}.json", "r+", encoding="utf-8") as f_1:
            data = json.load(f_1)
        comment = input(f"pls input {self.project_name} update comments: ")
        self.comments_dict[now] = comment
        data.update(self.comments_dict)
        with open(f"{self.project_name}.json", "w", encoding="utf-8") as f_2:
            json.dump(data, f_2, indent=2, ensure_ascii=False)
            print(f"This comment had been added: {comment}")
        return data       
   
    def comment_read(self):
        """Show all comments for project, return dict"""
        with open(f"{self.project_name}.json", "r") as f_3:
            comment_info = json.load(f_3)
            for j,k in comment_info.items():
                print(j + " comment is: " + k)
        return comment_info
    
    def creat_customer_path(self):
        "Creat a new path for new customer"
        os.mkdir(self.customer_name)
        self.customer_path = os.getcwd() + "\\" + self.customer_name
        return self.customer_path

    def change_to_customer_path(self):
        """Creat a path firstly"""
        os.chdir(self.customer_path)
        




if __name__ == "__main__":
    xinya = CustomerProject("xinya", "showroom")











    







        


 



















