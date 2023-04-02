package com.example.demo.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.entitydemo.UserDemo;
import com.example.demo.service.UserService;

@RestController
public class Controller {
	
	Logger logger = LoggerFactory.getLogger(Controller.class);
	
	@Autowired
	private UserService userService;
	
	@GetMapping("/")
	public String home() {
		logger.info("called the home page");
		return "API is working";
	}
	
	@GetMapping("/{id}")
	public UserDemo getUserById(@PathVariable("id") int id) {
		return userService.getUserById(id);
	}
	
	@PostMapping("/save")
	public UserDemo saveUser(@RequestBody UserDemo user) {
		return userService.saveUser(user);
	}
	
	@GetMapping("/getUsers")
	public List<UserDemo> getUsers(){
		return userService.getUsers();
	}
}
