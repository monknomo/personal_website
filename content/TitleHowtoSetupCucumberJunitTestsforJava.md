Title: How to Setup Cucumber Junit Tests for Java
Slug: how-to-setup-cucumber-junit-tests-for-java
Date: 5/4/2017 19:00
Modified: 5/4/2017 19:00
Category: Programming
Tags: java, cucumber, junit, testing, qa, qc
Authors: Gunnar Gissel
Summary: Cucumber requires 3 types of files to run as a junit test in Java - this article explains what they are and how to configure them

<a href="https://flic.kr/p/9xmxaQ"><img src="i.imgur.com/bgIGcnol.jpg" alt="cucumber growing" title="growing cucumber"></a>

Java cucumber tests have 3 parts.

1. The feature file
2. The step definitions (the 'glue' file(s))
3. The junit test file

The feature file is where the behavior, or business, oriented description of the test goes.  These files are written with Gherkin syntax.

When writing Cucumber tests, write the feature files first.  Have stakeholders, business owners and users write them, if that is possible in your organization.  If not, the lead developer and/or project manager should write the feature files with the stakeholders, business owners and users.  Put the work in and collect their stories and scenarios. 

After the feature file is written, write the step definitions.  This is what the Cucumber people call "glue" code.  It's essentially regexes, setup and test code.

Finally, to make running the Cucumber tests easy in Java, write a junit wrapper class.  This is an empty, annotated class that will enable Cucumber to use junit's test machinery to run Cucumber tests.

Example
-----------

I've created [an example project.](https://github.com/monknomo/Cucumber-Example-Art-Fight/)  Cucumber uses Maven, so we have a project with a standard Maven directory structure:

    +---src
    |   +---main
    |   |   +---java
    |   \---test
    |       +---java
    |       \---resources

###Organization

Let's put the feature files under test/resources.  Let's put the junit classes under the principal test package - in this case `com.gunnargissel.cucumberexample.artfight`.  Let's put the step definitions (the 'glue') in a stepdefs package under the principal test package - `com.gunnargissel.cucumberexample.artfight.stepdefs`

###Behavior Scenario

For this example, we are creating the business engine for an art supply store.  Let's use [Stuart Semple](stuartsemple.com/projects/black-v1-0-beta-worlds-mattest-flattest-black-art-material/) as an example.  Stuart Semple sells "Black 2.0 - The world's mattest, flattest, black art material" to everyone except [Anish Kapoor.](anishkapoor.com/)  There's [a bit of a backstory.](https://www.format.com/magazine/features/art/anish-kapoor-stuart-semple-vantablack-blackest-black)

Here's what a feature file might look like, `no_anish_kapoor.feature`:

    Feature: Stuart Semple will sell Black 2.0 to any artist except Anish Kapoor

        Scenario Outline: Anish Kapoor tries to buy Black 2.0
                           Given a purchaser, <purchaser name>, Black 2.0 is <saleable>
                           Examples:
                                     | purchaser name    | saleable     |
                                     | Anish Kapoor      | not saleable |
                                     | John Doe          | saleable     |
                                     | Jane Doe          | saleable     |
                                     | Manish Kapoor     | saleable     |
                                     | Anish Kapoorski   | saleable     |

With the feature file, it is time to create the step definitions, or 'glue' code.  In this case, create src/test/java/com.gunnargissel.blacktwopointoh.stepdefs.NoAnishKapoor.java

The scenario outlined above only uses one keyword, "Given".  That means we will create a single method in our step definition "glue" class that uses the `@Given` annotation.  The objective of the `@Given` annotation is to write a regular expression that matches the scenario.  In this case we want the `<purchaser name>` and the `<saleable>` qualities to be variables we pass to the stepdef.  The rest of the `@Given` is business language that we pattern match on.  The stepdef performs the role of a typical junit test, along with the setup for the test.

    @Given("^a purchaser, (.*), Black 2\\.0 is (not saleable|saleable)$")
                public void testWhoCanPurchaseBlackTwoPointOh(String purchaser, String saleable) {
                        boolean actual_saleable = BusinessRules.saleable(purchaser);
                        boolean expected_saleable = saleable.equals("saleable");
                        assertEquals(expected_saleable, actual_saleable);
                }
    
Now that there is a scenario and a step definition, a junit runner class needs to be created like so:

    @RunWith(Cucumber.class)
    @CucumberOptions(
                           format={"pretty", "junit:target/cucumber/black_two_point_oh_sales_list.xml"},
                            features = {"classpath:no_anish_kapoor.feature"},
                            glue={"com.gunnargissel.cucumberexample.artfight.stepdefs"}
    )
    public class TestBusinessRules {}
    
After creating the necessary files, running `mvn test` will execute the feature scenario created above.  Maven will create `black_two_point_oh_sales_list.xml` in the `target/cucumber` directory.

Further Resources
-------------------

[Just Enough Regular Expressions for Cucumber](agileforall.com/just-enough-regular-expressions-for-cucumber/) is a great guide that explains how to use regexes (and Java) with Cucumber.  The same author also made [a cheatsheet](agileforall.com/just-enough-regular-expressions-for-cucumber/) that is a helpful reference.

The [artfight example code.](https://github.com/monknomo/Cucumber-Example-Art-Fight/)

[_Thank you Ali Burçin Titizel for the header image_](https://flic.kr/p/9xmxaQ)