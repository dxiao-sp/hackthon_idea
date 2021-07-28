# Project Title

hackthon idea management 

## Description

This a practice project for hackthon idea management using django and graphql

## Getting Started


### Dependencies

* python 3.6.8, 
* MAC OS
* django

### Executing program

```
python manage.py runserver 
```
go to http://localhost:8000/graphq

```

Graphsql query:
#create new idea
```

mutation createMutation {
  createIdea(ideaData: {title: "Things Apart", description: "Chinua_Achebe@ta.com", eventName:"test", userId:3}) {
    idea {
      title,
      description,
      eventName,
      user:id
    }
  }
}
```
```
#create new user
mutation createMutation {
  createUser(userData: {name: "Things Apart", email: "Chinua_Achebe@ta.com"}) {
    user {
      name,
      email
    }
  }
}
```



## Authors

Contributors names and contact info

Dingwen Xiao
dxiao@tripadvisor.com

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

