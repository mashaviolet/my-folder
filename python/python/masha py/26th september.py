#operator and if else loops
#assignment operators we use = and can be used in calculations eg;
sum=0
sum+=0 #sum=sum+0
x=0
x+=5  #x=x+5
y=26
y+=5  #y=y+5
w=16
w//=8  #w=w//8
#sample
#given that we have 2 products a laptop and a mouse such that the price of a laptop is 300000 and the price of a mouse 
#is 50000 use a for loop to find the total sum of the products
laptop=300000
mouse=50000
product_prices=[laptop,mouse]
for price in product_prices:
    sum=0
    sum+=price
print(f"The total sum of the products is :{sum:,}")
#try removing the loop by removing the indentation
#and then move the sum=0 under loop 
# both give different answers