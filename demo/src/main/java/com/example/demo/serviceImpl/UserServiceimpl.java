package com.example.demo.serviceImpl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.entitydemo.UserDemo;
import com.example.demo.repository.UserRepo;
import com.example.demo.service.UserService;

@Service
public class UserServiceimpl implements UserService {
	
	@Autowired
	private UserRepo userRepo;

	@Override
	public UserDemo getUserById(int id) {
		// TODO Auto-generated method stub
		return userRepo.findById(id).get();
	}

	@Override
	public UserDemo saveUser(UserDemo user) {
		// TODO Auto-generated method stub
		return userRepo.save(user);
	}

	@Override
	public List<UserDemo> getUsers() {
		// TODO Auto-generated method stub
		return userRepo.findAll();
	}

}
