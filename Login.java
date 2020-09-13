package collection.map;

import java.util.*;

public class Login {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		List<Map<String, String>> userList = new ArrayList<>();
		
		System.out.println("*** Login ***");
		System.out.print("- ID registration: ");
		String uId = sc.next();
		System.out.print("- PW registration: ");
		String uPw = sc.next();
		Map<String, String> users = new HashMap<>();
		users.put(uId, uPw);
		
		userList.add(users);


		while(true) {

			System.out.println("----------------------");
			System.out.println("Enter your ID and password");
			System.out.print("ID: ");
			String id = sc.next();
			if(users.containsKey(id)) {
				System.out.print("PW: ");
				String pw = sc.next();
				String check = users.get(id);
				if(check.equals(pw)) {
					System.out.println("Login Success");
					break;
				}else {
					System.out.println("Wrong PW");
				}
			}else {
				System.out.println("ID not registered yet");
			}

		}
	}

}





