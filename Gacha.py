"""Gacha"""
import time
from random import choices
def main():
    """docsting"""
    box, rate_box, sr_box, sr_rate, ssr_box, ssr_rate, grade, get = [], [], [], [], [], [], [], []
    garuntee = 0


    while True:         #นำเข้าข้อมูลของ gacha โดยให้กรอก: ชื่อitem เรท% ถ้ากรอบครบแล้วให้พิมพ์ END
        item = input("Item:   ") #โดยที่ถ้าไม่สนใจของชิ้นไหนใน tier ให้รวม %ไปใน tier ได้เลย เช่น ตัวละครNo.1-->R แต่เราไม่สนใจให้รวมไปในเรท Rได้เลย
        while True:
            tier = input("Tier:   ")
            if tier.isdigit():
                print("Tier not digit!!!!!")
                continue
            else:
                break
        while True:
            rate = input("Rate:   ")
            if rate.isalpha():
                print("Rate not alpha!!!!!")
                continue
            else:
                break


        if tier == "SR" or tier == "SRR":#ประกัน 10
            sr_box.append(item)
            sr_rate.append(float(rate))
            if tier == "SRR": #ประกันใหญ่
                ssr_box.append(item)
                ssr_rate.append(float(rate))
        box.append(item)
        rate_box.append(float(rate))
        grade.append(tier)
        while True:
            ation = input("Complete?(Y/N)")
            if ation == "Y":
                break
            elif ation == "N":
                break
        if ation =="Y":
            break
        else:
            continue
    print(box)


    #rate_option = input("การคำนวณเรท:")#ในกรณีที่มีประกัน ถ้าเปิด10ครั้งรวด = No หรือ สะสมครบ10ครั้ง = YES
    garuntee_option = int(input("มีประกันrollที่:"))#ไม่มีให้ใส่-1
    #pickup_option = input("ประกันหน้าตู้ไหม:")#ออกหน้าตู้แน่นอน = YES
    roll_all = int(input("Open roll???:   "))
    for roll in range(1, roll_all+1):
        garuntee += 1
        if roll % 10 != 0:
            get.append(choices(box, weights=rate_box, k=1))
            if choices(box, weights=rate_box, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                garuntee = 0
        else:
            if garuntee == garuntee_option: #ได้ SSR แน่นอน การันตีจะรีกับไปที่ 0
                get.append(choices(ssr_box, weights=ssr_rate, k=1)) # สุ่ม SSR
                garuntee = 0
            else:
                get.append(choices(sr_box, weights=sr_rate, k=1)) # สุ่ม SR
                if choices(sr_box, weights=sr_rate, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                    garuntee = 0

    for i in range(len(get)):
        print(get[i][0])
        time.sleep(0.2)
    #print(choices(box, weights=rate_box, k=roll))
main()
