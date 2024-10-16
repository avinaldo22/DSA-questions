def containsDuplicate(nums :list) -> bool:
    
    nums.sort()

    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            return True
        
    return False


if __name__ == "__main__":

    arr = [4,5,6,6,7,8,10]

    condition = containsDuplicate(arr)

    print("The condition would be:", condition)