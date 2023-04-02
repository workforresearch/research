package com.example.demo.entitydemo;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
public class UserDemo {
	
	@Id
	@Column(name = "Id")
	private int id;
	private int age;
	private String name;
	private String address;
	
}
