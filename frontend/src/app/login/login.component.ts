import { Component, OnInit, Input } from '@angular/core';
import {LoginService} from "../login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  @Input() userSession: string;
  public username: string = "sbMemd7b5f5124626746c0765654ebe2c85048a5";
  public password: string = "sbMemd7b5f5124626746c0765654ebe2c85048a5#123";

  constructor(public service: LoginService) { }

  ngOnInit() {
  }

  login() {
    this.service.login(this.username, this.password).subscribe(
      (data) => {
        console.log(data);
      },
      (error) => console.log(error),
    )
  }

}
