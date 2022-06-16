import axios from 'axios'
import config from '@/config'

const baseURL= process.env.NODE_ENV=='development'?config.baseURL.dev:config.baseURL.pro

class HttpRequests{
    constructor(baseURL) {
        this.baseURL=baseURL
    }
    getInsideConfig(){
       const config={
           baseURL:this.baseURL,
           header:{}
       }
       return config
    }
    interceptors(instance){
        instance.interceptors.request.use(function (config){
            return config
        },function (error){
            return Promise.reject(error)
        });
        instance.interceptors.response.use(function (response){
            return response;
         },function (error){
            return Promise.reject(error)
        });
    }
    request(options){
        const instance = axios.create()
        options={
            ...this.getInsideConfig(),...options
        }
        this.interceptors(instance)
        return instance(options)
    }
}

export default new HttpRequests(baseURL)