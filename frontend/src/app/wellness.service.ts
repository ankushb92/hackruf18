import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { consts } from 'src/app/consts';

@Injectable({
    providedIn: 'root'
})
export class WellnessService {

    constructor(private http: HttpClient) { }
    get_wellness(session) {
        return this.http.get(consts.WELLNESS_URL, {headers: new HttpHeaders({'session': session})});
    }

    get_anal(session) {
      return this.http.get(consts.BASE_URL + '/transactions?tnonly', {headers: new HttpHeaders({'session': session})})
    }

    get_hold(session) {
      return this.http.get(consts.BASE_URL + '/holdings?tnonly', {headers: new HttpHeaders({'session': session})})
    }
}
