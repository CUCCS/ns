package com.example.activitytest;
import java.security.NoSuchAlgorithmException;
import java.lang.reflect.UndeclaredThrowableException;
import java.security.GeneralSecurityException;
import java.security.InvalidKeyException;
import java.sql.Date;
import java.util.Calendar;
import java.util.Random;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class Otp {
	private static final int[] doubleDigits =
        { 0, 2, 4, 6, 8, 1, 3, 5, 7, 9 };
	public static int calcChecksum(long num, int digits) {
		boolean doubleDigit = true;
		int     total = 0;
		while (0 < digits--) {
			int digit = (int) (num % 10);
			num /= 10;
			if (doubleDigit) {
				digit = doubleDigits[digit];
			}
			total += digit;
			doubleDigit = !doubleDigit;
		}
		int result = total % 10;
		if (result > 0) {
			result = 10 - result;
		}
		return result;
	}

    public static byte[] hmac_sha1(byte[] keyBytes, byte[] text)
            throws NoSuchAlgorithmException, InvalidKeyException
        {
            try {
                Mac hmacSha1;
                try {
                    hmacSha1 = Mac.getInstance("HmacSHA1");
                } catch (NoSuchAlgorithmException nsae) {
                    hmacSha1 = Mac.getInstance("HMAC-SHA-1");
                }
                SecretKeySpec macKey =
            new SecretKeySpec(keyBytes, "RAW");
                hmacSha1.init(macKey);
                return hmacSha1.doFinal(text);
            } catch (GeneralSecurityException gse) {
                throw new UndeclaredThrowableException(gse);
            }
        }




	private static final int[] DIGITS_POWER
	= {1,10,100,1000,10000,100000,1000000,10000000,100000000};

	static public String generateOTP(byte[] secret,
			long movingFactor,
			int codeDigits,
			boolean addChecksum,
			int truncationOffset)
					throws NoSuchAlgorithmException, InvalidKeyException
	{
		// put movingFactor value into text byte array
		String result = null;
		int digits = addChecksum ? (codeDigits + 1) : codeDigits;
		byte[] text = new byte[8];
		for (int i = text.length - 1; i >= 0; i--) {
			text[i] = (byte) (movingFactor & 0xff);
			movingFactor >>= 8;
		}
		byte[] hash = hmac_sha1(secret, text);
		int offset = hash[hash.length - 1] & 0xf;
		if ( (0<=truncationOffset) &&
				(truncationOffset<(hash.length-4)) ) {
			offset = truncationOffset;
		}
		int binary =
	((hash[offset] & 0x7f) << 24)
	| ((hash[offset + 1] & 0xff) << 16)
	| ((hash[offset + 2] & 0xff) << 8)
	| (hash[offset + 3] & 0xff);


		int otp = binary % DIGITS_POWER[codeDigits];
		if (addChecksum) {
			otp =  (otp * 10) + calcChecksum(otp, codeDigits);
		}
		result = Integer.toString(otp);
		while (result.length() < digits) {
			result = "0" + result;
		}
		return result;
	}

	private final static String NUM_CHAR = "0123456789";  

	private static int charLen = NUM_CHAR.length();  

	/**  

	    * 根据系统时间获得指定位数的随机数  

	    * @param randomNumberDigit 随机数的位数  

	    *  @return  获得的随机数  

	    */  

	   public static String getRandomNumber(int randomNumberDigit) {  

	      long seed = System.currentTimeMillis();// 获得系统时间，作为生成随机数的种子  
	      seed=seed/1000/60;
	      //System.out.println("otp时间："+seed);
	      StringBuffer sb = new StringBuffer();// 装载生成的随机数  

	      Random random = new Random(seed);// 调用种子生成随机数  

	      for (int i = 0; i < randomNumberDigit; i++) {  

	         sb.append(NUM_CHAR.charAt(random.nextInt(charLen)));  

	      }  

	return sb.toString();  

	   }

}
