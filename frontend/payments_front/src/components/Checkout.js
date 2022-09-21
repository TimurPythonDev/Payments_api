import React,{useState, useEffect} from 'react'
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";
import { useParams } from 'react-router-dom';
import PaymentForm from './PaymentForm';



const stripePromise = loadStripe("pk_test_51LjMUsF6Mp7xfqZYh1VtGHTtaVOPvnN9T5IszRn7VH4PSD3F537YxGKqWq0nv0vLFjx4oCGh8IgxM50HsDmZb7cj00HDRsEGD1");

const Checkout = () => {
   
    const [clientsecret, setClientSecret]=useState('')
    const {prod_id}=useParams();
    console.log(prod_id)
    useEffect(()=>{
        fetch("http://127.0.0.1:8000/api/create-payment-intent/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(prod_id),
          })
            .then((res) => res.json())
            .then((data) => setClientSecret(data.clientSecret));
    }, [])
    
    const appearance = {
        theme: 'stripe',
      };
      const options = {
        clientSecret:clientsecret
      };

      

     
  return (
    <div className='container'>
        {clientsecret && (
        <Elements  stripe={stripePromise} options={options}>
             <PaymentForm/>
        </Elements>
      )}
    </div>
  )
}

export default Checkout