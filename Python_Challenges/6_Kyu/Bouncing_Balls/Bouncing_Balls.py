def bouncing_ball(h, bounce, window):
    see_ball = 0
    ball_height = h
    
    #Parameter Check
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        
        while ball_height > window:
            
            see_ball += 1
            ball_height *= bounce
            
            if ball_height > window:
                see_ball += 1
            else:
                break
    else:
        see_ball = -1
    
    return see_ball
