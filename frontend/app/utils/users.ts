import axios, { AxiosError } from 'axios'

export interface User { 
    username: string, 
    email: string,
    password: string,
    mobile: string,
    role: string
}

export const base_url = 'http://localhost:8000/v1'
export const addUser = async (user: User) => { 
    try { 
        const response = await axios.post(`${base_url}/users`, { ...user})
        return response
    } catch(err) { 
        if(err instanceof AxiosError) return err.response 
    }
}

export const login = async(email: string, password : string) => { 
    try { 
        const response = await axios.post(`${base_url}/auth/login`, { email , password})
        return response
    } catch(err) { 
        if(err instanceof AxiosError) return err.response 
    }
}