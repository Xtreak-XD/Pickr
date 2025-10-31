import {React, useState} from 'react'
import Confetti from "react-confetti";


export const ConfettiEffect = ({width, height}) => {

    return (
        <div>
            <Confetti
                width={width}
                height={height}
                numberOfPieces={600}
                gravity={0.8}
            />
        </div>
    )
}
