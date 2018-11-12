

import random
import arcade
import os
import pyglet

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SPRITE_SCALING_COIN = 0.2
BRICK_COUNT = 30
X_POS = 200
Y_POS = 500
MOVEMENT_SPEED = 5
#SOUNDS = {'wing': arcade.load_sound("am.mp3"),
       # 'wing2': arcade.load_sound("wing.ogg")}


class MyGame(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
    
    	#arcade.play_sound(SOUNDS['wing'])
    	# dict mapping sound name to arcade sound object
    	self.explosion = pyglet.media.load('exp.mp3', streaming=False)
	
    	
    	self.movementspeed1 = 3
    	self.TAB = 0
    	self.brick_list = arcade.SpriteList()
    	self.temp_list = arcade.SpriteList()
    	self.dish = arcade.SpriteList()
    	self.ball = arcade.SpriteList()
    	# Score
    	self.score = 0
    	# Set up the player
    	self.dish_sprite = arcade.Sprite("dish.png", 0.6)
    	self.dish_sprite.center_x = 500 # Starting position
    	self.dish_sprite.center_y = 100
    	self.dish.append(self.dish_sprite)
    	self.ball_sprite = arcade.Sprite("ball.png", 0.4)
    	
    	
    	self.ball_sprite.center_x = random.choice([100, 200, 300, 400, 500])
    	self.ball_sprite.center_y = 200
		
	
    	self.ball.append(self.ball_sprite)
    	temp = 0
    	ytemp = 0
    	self.physics_engine = arcade.PhysicsEngineSimple(self.dish_sprite, self.brick_list)
    	self.physics_engine2 = arcade.PhysicsEngineSimple(self.ball_sprite, self.temp_list)
    	for i in range(5):
    		temp = 0
    		for j in range(12):
    			self.brick_sprite = arcade.Sprite("brick.png", SPRITE_SCALING_COIN)
    			self.brick_sprite.center_x = 200 + temp
    			self.brick_sprite.center_y = 500 + ytemp
    			self.brick_list.append(self.brick_sprite)
    			temp = temp + 55
    		ytemp = ytemp - 55
    		
    	if len(self.brick_list) < 1:
    		for i in range(4):
    			temp = 0
    		for j in range(9):
    			self.brick_sprite = arcade.Sprite("brick.png", SPRITE_SCALING_COIN)
    			self.brick_sprite.center_x = 200 + temp
    			self.brick_sprite.center_y = 500 + ytemp
    			self.brick_list.append(self.brick_sprite)
    			temp = temp + 75
    		ytemp = ytemp - 75
    		

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.brick_list.draw()
        self.dish.draw()
        self.ball.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 470, 550, arcade.color.AMAZON, 14)
        
        if self.TAB == 1:
        	arcade.draw_text("GAME OVER", 300, 350, arcade.color.AMAZON, 50)
        	
        if len(self.brick_list) < 1 and self.TAB == 0:
        	arcade.draw_text("YOU WIN", 310, 350, arcade.color.AMAZON, 50)
        	

    def update(self, delta_time):
        self.physics_engine.update()
        self.physics_engine2.update()
        
        self.brick_list.update()
        bricks_hit_list = arcade.check_for_collision_with_list(self.ball_sprite, self.brick_list)
        
        if(len(bricks_hit_list) > 0):
        	self.explosion.play()
        	
        	
       
        for brick in bricks_hit_list:
        	brick.kill()
        	self.score += 1
        
        
        
        if len(arcade.check_for_collision_with_list(self.ball_sprite, self.dish)) > 0:
        	self.ball_sprite.change_y = -self.ball_sprite.change_y
        	#arcade.play_sound(SOUNDS['wing2'])
        	#self.explosion.play()
        
        if self.dish_sprite.center_x == 10:
        	self.dish_sprite.change_x = MOVEMENT_SPEED 
        	
        if self.dish_sprite.center_x == 990:
        	self.dish_sprite.change_x = -MOVEMENT_SPEED 
        	
        if self.ball_sprite.center_x <= 10 or self.ball_sprite.center_x >= 990:
        	self.ball_sprite.change_x = -self.ball_sprite.change_x
        	
        if self.ball_sprite.center_y <= 10 or self.ball_sprite.center_y >= 600:
        	self.ball_sprite.change_y = -self.ball_sprite.change_y
        	
        if self.TAB == 0 and self.ball_sprite.change_x == 0:
        	self.ball_sprite.change_x = self.movementspeed1
        	self.ball_sprite.change_y = self.movementspeed1
        	
        if self.ball_sprite.center_y <= 95 :
        	self.TAB = 1
        	self.ball_sprite.change_x = 0
        	self.ball_sprite.change_y = 0
        	self.ball_sprite.center_x = 500
        	self.ball_sprite.center_y = 200
        	self.dish_sprite.change_x = 0
        	self.dish_sprite.change_x = 0
        	
        	while len(self.brick_list) > 0:
        		for i in self.brick_list:
        			i.kill()
        	
        	for i in self.dish:
        		i.kill()
        		
        		
        if len(self.brick_list) < 1 and self.TAB == 0:
        	self.ball_sprite.change_x = 0
        	self.ball_sprite.change_y = 0
        	self.ball_sprite.center_x = 500
        	self.ball_sprite.center_y = 200
        	self.dish_sprite.change_x = 0
        	self.dish_sprite.change_x = 0
        	
        	while len(self.brick_list) > 0:
        		for i in self.brick_list:
        			i.kill()
        		
        	
        	self.ball_sprite.change_x = 0
        	self.ball_sprite.change_y = 0
        	self.ball_sprite.center_x = 500
        	self.ball_sprite.center_y = 200
        	self.dish_sprite.change_x = 0
        	self.dish_sprite.change_x = 0
        	
        	while len(self.brick_list) > 0:
        		for i in self.brick_list:
        			i.kill()
        	
        	for i in self.dish:
        		i.kill()
        
        
    def on_key_press(self, key, modifiers):
    	
    	if(len(self.dish) > 0):
	    	if key == arcade.key.UP:
	    		self.dish_sprite.change_y = 0
	    	elif key == arcade.key.DOWN:
	    		self.dish_sprite.change_y = 0
	    	elif key == arcade.key.LEFT:
	    		self.dish_sprite.change_x = -MOVEMENT_SPEED
	    	elif key == arcade.key.RIGHT:
	    		self.dish_sprite.change_x = MOVEMENT_SPEED


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    


if __name__ == "__main__":
    main()
