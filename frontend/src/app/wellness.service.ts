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
}
