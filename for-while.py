for
- строка
- список
- словарь
- функция range
- любой итерируемый обьект

vlan_list = [1,2,3,4]
for vlan in vlan_list:

range(1,5)
[1,2,3,4]
for number in range(10):
    print(f"interface Gi0/{number}")

for key, value in r1.items():
    print(key, value)

for intf fast_int:
    print("interface {intf}")
----------------------------------------------------
commands = [
    "switchport mode access",
    "switchport acess vlan"
    ]

access = {'0/12' : 10, '0/14': 11, '0/16' : 17, '0/17' : 150}

for intf, vlan in access.items():
    print(f"interface {intf}")
    for cmd in commands:
        if cmd.endswitch("vlan"):
            print(f" {cmd} {vlan}")
        else:
            print(f" {cmd}")

----------------------------------------------------while
a = 5
while a > 0:
  print(a)
  a -= 1
5
4
3
2
1
