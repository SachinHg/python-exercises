def find132pattern(nums)
    i=0
    while i < nums.length - 2
    	p "::::::::::#{nums[i]}:::::::#{nums[i+1]}:::::::#{nums[i+2]}"
        if nums[i] < nums[i+2] and nums[i+1] > nums[i+2] and nums[i] < nums[i+1]
            return true
            break
        end
        i+=1
    end
    return false
end

nums = [3,5,0,3,4]
ans = find132pattern(nums)
puts(ans)