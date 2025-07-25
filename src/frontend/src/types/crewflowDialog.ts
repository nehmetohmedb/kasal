import { Node, Edge } from 'reactflow';
import { FlowConfiguration } from './flow';

export interface CrewFlowSelectionDialogProps {
  open: boolean;
  onClose: () => void;
  onCrewSelect: (nodes: Node[], edges: Edge[], crewName?: string, crewId?: string) => void;
  onFlowSelect: (nodes: Node[], edges: Edge[], flowConfig?: FlowConfiguration) => void;
  initialTab?: number;
} 