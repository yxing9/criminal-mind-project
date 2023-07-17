# Criminal Mind Project

Project under the Computer Science Department of the University of Wisconsin-Whitewater. 

This repository contains a data processing pipeline to create a comprehensive database of serial killers. The data is extracted from publicly available sources and processed into structured CSV files. The database is designed to assist detectives, researchers, and other interested parties in studying and analyzing serial killer cases.

## Database Schema
CREATE TABLE Killers (
	killer_id int NOT NULL,
	killer_first_name text NOT NULL,
	killer_last_name text NOT NULL,
	PRIMARY KEY (killer_id)
);
# victims table
CREATE TABLE Victims (
	victim_id int NOT NULL,
	killer_id int NOT NULL,
	rape tinyint NOT NULL,
	tortured_victims tinyint NOT NULL,
	stalked_victims tinyint NOT NULL,
	overkill tinyint NOT NULL,
	quick_and_efficient tinyint NOT NULL,
	used_blindfold tinyint NOT NULL,
	bound_victims tinyint NOT NULL,
	sex_with_body tinyint NOT NULL,
	mutilated_body tinyint NOT NULL,
	ate_part_of_body tinyint NOT NULL,
	drank_victims_blood tinyint NOT NULL,
	posed_body tinyint NOT NULL,
	took_totem_body_part tinyint NOT NULL,
	took_totem_personal_item tinyint NOT NULL,
	robbed_victim_or_location tinyint NOT NULL,
	left_at_scene_no_attempt_to_hide tinyint NOT NULL,
	left_at_scene_hidden tinyint NOT NULL,
	left_at_scene_buried tinyint NOT NULL,
	moved_no_attempt_to_hide tinyint NOT NULL,
	moved_buried tinyint NOT NULL,
	cut_up_and_disposed_of tinyint NOT NULL,
	moved_to_home tinyint NOT NULL,
	PRIMARY KEY (victim_id),
	FOREIGN KEY (killer_id)
);
# life events table
CREATE TABLE Life_events(
	event_id int NOT NULL,
	killer_id int NOT NULL,
	victim_id int NOT NULL,
	age int NOT NULL,
	physical_abuse tinyint,
	sexual_abuse tinyint,
	physiological_abuse tinyint,
	lust tinyint,
	power tinyint,
	anger tinyint,
	adopted tinyint,
	cross_dressed_as_kid tinyint,
	convicted tinyint,
	arrested tinyint,
	sentenced tinyint,
	stealing tinyint,

	reward float,
	PRIMARY KEY (event_id),
	FOREIGN KEY (killer_id),
	FOREIGN KEY(victim_id)
);

## How to Use the Database
As a user of the Serial Killers Profiling Database, you can perform various research tasks:

Search: Use spreadsheet software or a custom application to search for serial killers by name, location, number of victims, or any other attribute.

Filter and Sort: Apply filters to view data based on specific criteria, such as the date of the crime, victim profile, or modus operandi. Sort the data by different attributes like the number of victims, date, or other characteristics.

Visualize: Create visualizations such as maps, timelines, or bar charts to show the geographic distribution of serial killers, the time frame of their activities, or other patterns in the data.

Compare: Compare multiple serial killers side-by-side, highlighting similarities and differences between their profiles, modus operandi, or other attributes.

Analyze: Conduct statistical analyses or use machine learning techniques to identify patterns, trends, or correlations within the data. This could help in solving cold cases or providing insights into the behavior and motivations of serial killers.

Collaborate: Share your findings with other users or collaborate with other researchers, detectives, or experts in the field.

By using the Serial Killers Profiling Database, you can gain insights into the world of serial killers and potentially contribute to solving open cases or furthering the understanding of these heinous crimes.
