import {BsBell} from "react-icons/bs";
import {IconButton} from "@chakra-ui/react";

export function BellIcon() {
    return(
        <IconButton
            _hover={{
                background: "white",
            }}
            colorScheme='purple'
            aria-label='AiOutlineHome2'
            height='50px'
            width='50px'
            variant='ghost'
            icon={<BsBell/>}>
        </IconButton>
    )
}