import vk
profiles = vkapi.users.get(user_id=1)
print(profiles[0]['last_name'])
