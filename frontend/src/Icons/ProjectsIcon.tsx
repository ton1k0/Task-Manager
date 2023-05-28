import {
    Box,
    Flex,
    IconButton,
    Text,
    Tabs, Tab, TabPanel,
} from "@chakra-ui/react";
import {BsFolder} from "react-icons/all";


export function ProjectsIcon() {
    return(
        <Flex>
        <Tabs>
            <Tab>
                <IconButton
                    _hover={{
                        background: "white",
                    }}
                    colorScheme='purple'
                    aria-label='BsFolder'
                    height='50px'
                    width='50px'
                    variant='ghost'
                    icon={<BsFolder/>}>
                    <label htmlFor="nav-toggle" className="navToggle"></label>
                </IconButton>
            </Tab>
            <TabPanel>
                    <Flex
                        marginLeft={"75px"}>
                        <h2 className="logo">Active</h2>
                                <Box
                                    maxW='sm'
                                     maxH='sm'
                                     borderWidth='1px'
                                     borderRadius='lg'
                                     overflow='hidden'
                                >

                                    <Text fontSize={60}
                                          fontWeight="extrabold"
                                    >

                                        Black Angus

                                    </Text>
                                </Box>
                    </Flex>
                </TabPanel>
            </Tabs>
        </Flex>
    )
}