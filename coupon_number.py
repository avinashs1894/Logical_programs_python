import random


class Coupan:

    
    try:
            def generate(amount):

                coupon = open("coupons.txt", "a")  

                for x in range(0, amount):

                    a = random.randint(1000, 9999)
                    a = str(a)
                     
                    coupon.write(a)
                    coupon.write("\n")
        
            if __name__ == "__main__" :
                amount = int(input("How many coupons do you want to generate: "))

                generate(amount)
            print("\nCode's have been generated!")    

    except ValueError:            
            print("\n please enter digit amount only")