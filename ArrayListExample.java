package collection.list;

import java.util.*;

public class ArrayListExample {

	public static void main(String[] args) {
		
		List<String> list = new ArrayList<>();
		
		String str1 = "Java";
		String str2 = "JSP";
		
		System.out.println(list);
		
		list.add(str1);
		list.add(str2);
		list.add("DataBase");
		list.add("JDBC");
		list.add("JSP");
		
		System.out.println(list);
		

		int size = list.size();
		System.out.println("Object saved in list: " + size);
		
		list.add(2, "Oracle");
		System.out.println(list);
		

		
		list.set(3, "MySQL");
		System.out.println(list);
		

		String s = list.get(2);
		System.out.println("2번 인덱스 객체: " + s);
		

		int idx = list.indexOf("MySQL");
		System.out.println("MySQL이 저장된 인덱스: " + idx);
		

		idx = list.indexOf("안녕~~");
		System.out.println(idx);
		

		list.remove(5);
		System.out.println(list);
		
		list.remove(str1);
		System.out.println(list);
		

		System.out.println(list.contains("JSP"));
		System.out.println(list.contains(str2));
		System.out.println(list.contains("Alert!"));
		

		System.out.println("--------------------------");
		for(int i=0; i<list.size(); i++) {
			System.out.println(list.get(i));
		}
		System.out.println("--------------------------");
		for(String str : list) {
			System.out.println(str);
		}
		

		list.clear();
		System.out.println(list);
		

		if(list.isEmpty()) {
			System.out.println("list가 비어있음.");
		}else {
			System.out.println("list가 비어있지 않음.");			
		}

	}

}



