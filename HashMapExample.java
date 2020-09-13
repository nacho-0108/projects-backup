package collection.map;

import java.util.*;

public class HashMapExample {

	public static void main(String[] args) {
		
		Map<String, Integer> map = new HashMap<>();
		

		map.put("Chicken", 20000);
		map.put("Ramen", 2000);
		map.put("Chips", 30000);

		map.put("Ramen", 3000); 
		
		System.out.println(map);
		

		System.out.println("n of object in map: " + map.size());
		

		int price = map.get("Chips");
		System.out.printf("price of chips: %d원\n", price);

		Set<String> kSet = map.keySet();
		System.out.println(kSet);
		
		Iterator<String> kIter = kSet.iterator();
		System.out.println("----------------------");
		
		while(kIter.hasNext()) {
			String foodName = kIter.next();
			int foodPrice = map.get(foodName);
			System.out.printf("%s의 가격은 %d원입니다.\n",
					foodName, foodPrice);
		}
		

		String food = "감자";
		
		if(map.containsKey(food)) {
			System.out.println("price of " + food 
					+ map.get(food));
		} else {
			System.out.println(food + "does not exist");
		}
		

		map.remove("Chicken");
		System.out.println(map);
		
		map.clear();
		
		if(map.isEmpty()) {
			System.out.println("map empty");
		}else {
			System.out.println("map not empty");			
		}
		
	}

}



