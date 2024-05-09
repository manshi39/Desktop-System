import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final TextEditingController _nameController = TextEditingController();

  Future<void> _activateDesktop(String name) async {
    final String url = 'http://127.0.0.1:9102/activate_desktop'; // Replace with your server URL
    try {
      final response = await http.post(
        Uri.parse(url),
        body: {'name': name},
      );
      if (response.statusCode == 200) {
        print('Desktop activated successfully');
        // Handle success
      } else {
        print('Failed to activate desktop - Status code: ${response.statusCode}');
        // Handle failure
      }
    } catch (e) {
      print('Error activating desktop: $e');
      // Handle error
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Activate Desktop'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              TextField(
                controller: _nameController,
                decoration: InputDecoration(labelText: 'Enter your name'),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {
                  String name = _nameController.text.trim();
                  if (name.isNotEmpty) {
                    _activateDesktop(name);
                  } else {
                    // Handle empty name input
                    print('Please enter your name');
                  }
                },
                child: Text('Activate Desktop'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
