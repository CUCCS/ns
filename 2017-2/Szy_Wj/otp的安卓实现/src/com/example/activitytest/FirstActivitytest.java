package com.example.activitytest;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

import android.util.Log;
import com.example.activetest.R;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.Window;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.TextView.OnEditorActionListener;
import android.widget.Toast;

public class FirstActivitytest extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(R.layout.first_layout);
		final EditText editText=(EditText)findViewById(R.id.editText1);  
        final TextView textview=(TextView)findViewById(R.id.textView1);
        //获取EditText文本  
        Button button1=(Button)findViewById(R.id.getotp);  
        button1.setOnClickListener(new OnClickListener() {  
            @Override  
            public void onClick(View v) {  
            	byte[] a=null;
            	a=editText.getText().toString().getBytes();
            	String b = null;
            	String c = null;
            	String d =null;
            	Otp s= new Otp();
            	try {
            		d=s.getRandomNumber(6);
            		int i = Integer.parseInt(d);  
        			b = s.generateOTP(a,i , 5, true,0);
        			//c =s.generateOTP(a,i, 5, true, 0);
        			System.out.println("otp口令："+b);
        		} catch (InvalidKeyException e) {
        			// TODO Auto-generated catch block
        			e.printStackTrace();
        		} catch (NoSuchAlgorithmException e) {
        			// TODO Auto-generated catch block
        			e.printStackTrace();
        		}
            	textview.setText(b);
            	
                 
            }  
        });  
		//Button button1=(Button)findViewById(R.id.getotp);
		
		
		
		/*button1.setOnClickListener(new OnClickListener(){
			public void onClick(View v){
				//Toast.makeText(FirstActivitytest.this, "You clicked botton1", Toast.LENGTH_SHORT).show();
				//Intent intent=new Intent(FirstActivitytest.this,SecondActivitytest.class);
				//startActivity(intent);
				Intent intent = new Intent(Intent.ACTION_VIEW);
				intent.setData(Uri.parse("http://www.baidu.com"));
				startActivity(intent);
			}
		});
	}
	*/
	}
	public boolean onCreateOptionsMenu(Menu menu){
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	public boolean onOptionsItemSelected(MenuItem item){
		switch(item.getItemId()){
		case R.id.add_item:
			Toast.makeText(this,"ADD",Toast.LENGTH_SHORT).show();
			break;
		case R.id.remove_item:
			Toast.makeText(this,"REMOVE",Toast.LENGTH_SHORT).show();
			break;
		default:
		}
		return true;
	}
	
}

