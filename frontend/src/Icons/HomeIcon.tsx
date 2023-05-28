import {AiOutlineHome} from "react-icons/ai";
import {IconButton} from "@chakra-ui/react";

export function HomeIcon() {
    return(
        <IconButton
            _hover={{
                background: "white",
            }}
            colorScheme='purple'
            aria-label='AiOutlineHome'
            height='50px'
            width='50px'
            variant='ghost'
            icon={<AiOutlineHome/>}>
        </IconButton>
    )
}