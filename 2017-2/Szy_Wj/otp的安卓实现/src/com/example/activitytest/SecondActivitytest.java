package com.example.activitytest;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import com.example.activetest.R;

import android.app.Activity;
import android.os.Bundle;
import android.view.Window;

public class SecondActivitytest extends Activity{
	@Override
	protected void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		byte[] a={1,1,0,1,1,1};		
    	String b = null;
    	Otp s= new Otp();
    	try {
			b = s.generateOTP(a, 102638465, 5, true, 3);
			System.out.println("otp¿ÚÁî£º"+b);
		} catch (InvalidKeyException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (NoSuchAlgorithmException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	System.out.println("otp¿ÚÁî£º"+b);
		//requestWindowFeature(Window.FEATURE_NO_TITLE);
		setContentView(R.layout.second_layout);
	}


}