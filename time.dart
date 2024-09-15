class Food {
  final String id;
  final String foodname;
  final DateTime date;
  int awli_vote;
  int khob_vote;
  int bad_vote;
  int eftezah_vote;
  bool userVoted;
  final String foodType;

  Food({
    required this.id,
    required this.foodname,
    required this.date,
    required this.awli_vote,
    required this.khob_vote,
    required this.bad_vote,
    required this.eftezah_vote,
    required this.userVoted,
    required this.foodType,
  });

  // Calculate the average rating
  double get averageRating {
    int totalVotes = awli_vote + khob_vote + bad_vote + eftezah_vote;
    if (totalVotes == 0) return 0.0;
    return (awli_vote * 4 + khob_vote * 3 + bad_vote * 2 + eftezah_vote * 1) / totalVotes;
  }
}

class FoodSummary {
  final String foodname;
  final String foodType;
  final double averageRating;

  FoodSummary({
    required this.foodname,
    required this.foodType,
    required this.averageRating,
  });

  @override
  String toString() {
    return 'Food: $foodname, Type: $foodType, Average Rating: $averageRating';
  }
}


void main() {
  List<Food> foods = [
    Food(
      id: '1',
      foodname: 'Pizza',
      date: DateTime.now(),
      awli_vote: 20,
      khob_vote: 30,
      bad_vote: 10,
      eftezah_vote: 5,
      userVoted: true,
      foodType: 'Italian',
    ),
    Food(
      id: '2',
      foodname: 'Burger',
      date: DateTime.now(),
      awli_vote: 15,
      khob_vote: 25,
      bad_vote: 8,
      eftezah_vote: 2,
      userVoted: true,
      foodType: 'Fast Food',
    ),
    Food(
      id: '3',
      foodname: 'Pizza',
      date: DateTime.now(),
      awli_vote: 10,
      khob_vote: 20,
      bad_vote: 5,
      eftezah_vote: 2,
      userVoted: true,
      foodType: 'Italian',
    ),
  ];

  // Group by food name
  Map<String, List<Food>> groupedFoods = {};
  for (var food in foods) {
    if (!groupedFoods.containsKey(food.foodname)) {
      groupedFoods[food.foodname] = [];
    }
    groupedFoods[food.foodname]!.add(food);
  }

  // Calculate average ratings for each group
  List<FoodSummary> summaries = [];
  groupedFoods.forEach((foodname, foodList) {
    String foodType = foodList.first.foodType;
    double totalRating = 0.0;

    for (var food in foodList) {
      totalRating += food.averageRating;
    }

    double averageRating = totalRating / foodList.length;
    summaries.add(FoodSummary(
      foodname: foodname,
      foodType: foodType,
      averageRating: averageRating,
    ));
  });

  // Print summaries
  for (var summary in summaries) {
    print(summary);
  }
}
