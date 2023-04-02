package com.example.demo.service;

import java.util.List;

import com.example.demo.entitydemo.UserDemo;

public interface UserService {

	UserDemo getUserById(int id);

	UserDemo saveUser(UserDemo user);

	List<UserDemo> getUsers();

}
